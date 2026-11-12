"""Entrenamiento reproducible, GridSearchCV y tracking MLflow."""
from pathlib import Path
import os, json, hashlib
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV, cross_val_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,roc_auc_score,ConfusionMatrixDisplay,RocCurveDisplay
import mlflow
import mlflow.sklearn
from datos_prep import preparar

ROOT=Path(__file__).resolve().parents[1]
SEED=42

def main():
    df=preparar(ROOT)
    X=df.drop(columns=['y']); y=df['y']
    numeric=X.select_dtypes(include='number').columns.tolist()
    categorical=X.select_dtypes(exclude='number').columns.tolist()
    pre=ColumnTransformer([
        ('num',Pipeline([('imputer',SimpleImputer(strategy='median')),('scaler',StandardScaler())]),numeric),
        ('cat',Pipeline([('imputer',SimpleImputer(strategy='most_frequent')),('onehot',OneHotEncoder(handle_unknown='ignore'))]),categorical)
    ])
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.2,random_state=SEED,stratify=y)
    cv=StratifiedKFold(n_splits=5,shuffle=True,random_state=SEED)
    models={
        'Regresion_logistica':(LogisticRegression(max_iter=1500,random_state=SEED),{'model__C':[0.1,1.0,10.0],'model__class_weight':[None,'balanced']}),
        'Random_forest':(RandomForestClassifier(random_state=SEED,n_jobs=1),{'model__n_estimators':[100,200],'model__max_depth':[8,16],'model__min_samples_leaf':[1,5]})
    }
    tracking=os.environ.get('MLFLOW_TRACKING_URI', 'sqlite:////content/mlflow.db')
    mlflow.set_tracking_uri(tracking)
    mlflow.set_experiment('Actividad5_Banca')
    (ROOT/'resultados').mkdir(exist_ok=True)
    (ROOT/'graficas').mkdir(exist_ok=True)
    results=[]; cv_details={}
    for name,(model,grid) in models.items():
        pipe=Pipeline([('prep',pre),('model',model)])
        search=GridSearchCV(pipe,grid,cv=cv,scoring='f1',n_jobs=-1,refit=True,return_train_score=False)
        with mlflow.start_run(run_name=name):
            search.fit(X_train,y_train)
            fitted=search.best_estimator_
            pred=fitted.predict(X_test)
            proba=fitted.predict_proba(X_test)[:,1]
            metrics={'accuracy':accuracy_score(y_test,pred),'precision':precision_score(y_test,pred,zero_division=0),'recall':recall_score(y_test,pred,zero_division=0),'f1':f1_score(y_test,pred,zero_division=0),'roc_auc':roc_auc_score(y_test,proba)}
            folds=cross_val_score(fitted,X_train,y_train,scoring='f1',cv=cv,n_jobs=-1)
            row={'modelo':name,**metrics,'cv_f1_mean':float(folds.mean()),'cv_f1_std':float(folds.std(ddof=1)),'best_params':json.dumps(search.best_params_,ensure_ascii=False)}
            results.append(row)
            cv_details[name]=folds.tolist()
            mlflow.log_params({k.replace('model__',''):str(v) for k,v in search.best_params_.items()})
            mlflow.log_param('dataset','UCI bank-full.csv sin duration')
            mlflow.log_param('test_size',.2)
            mlflow.log_param('cv_folds',5)
            mlflow.log_param('random_state',SEED)
            mlflow.log_metrics({**metrics,'cv_f1_mean':row['cv_f1_mean'],'cv_f1_std':row['cv_f1_std']})
            fig,ax=plt.subplots(figsize=(6,4))
            ConfusionMatrixDisplay.from_predictions(y_test,pred,ax=ax,cmap='Blues',colorbar=False)
            fig.tight_layout(); out=ROOT/'graficas'/f'matriz_{name}.png';fig.savefig(out,dpi=150);plt.close(fig);mlflow.log_artifact(str(out),'graficas')
            fig,ax=plt.subplots(figsize=(6,4))
            RocCurveDisplay.from_predictions(y_test,proba,ax=ax)
            fig.tight_layout();out=ROOT/'graficas'/f'roc_{name}.png';fig.savefig(out,dpi=150);plt.close(fig);mlflow.log_artifact(str(out),'graficas')
            mlflow.sklearn.log_model(fitted,name='modelo')
            print(name,metrics,search.best_params_)
    res=pd.DataFrame(results)
    res.to_csv(ROOT/'resultados'/'comparacion_modelos.csv',index=False)
    (ROOT/'resultados'/'cv_folds.json').write_text(json.dumps(cv_details,indent=2))
    fig,ax=plt.subplots(figsize=(8,4));res.set_index('modelo')[['accuracy','precision','recall','f1','roc_auc']].T.plot.bar(ax=ax,ylim=(0,1.05));ax.set_ylabel('Puntuacion');fig.tight_layout();fig.savefig(ROOT/'graficas'/'comparacion_metricas.png',dpi=150);plt.close(fig)
    fig,ax=plt.subplots(figsize=(5,3));y.value_counts().sort_index().plot.bar(ax=ax);ax.set_xticklabels(['No','Si'],rotation=0);ax.set_title('Contratacion de deposito');fig.tight_layout();fig.savefig(ROOT/'graficas'/'distribucion_clases.png',dpi=150);plt.close(fig)
    fig,ax=plt.subplots(figsize=(6,3));df.boxplot(column='balance',ax=ax);ax.set_title('Saldo: valores extremos');fig.tight_layout();fig.savefig(ROOT/'graficas'/'balance_outliers.png',dpi=150);plt.close(fig)
    print('Resultados guardados en',ROOT/'resultados')
    print('Tracking MLflow:',tracking)

if __name__=='__main__': main()
