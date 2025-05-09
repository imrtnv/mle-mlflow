# задаём название эксперимента и имя запуска для логирования в MLflow

EXPERIMENT_NAME = "churn_fio"
RUN_NAME = "data_check"

# создаём новый эксперимент в MLflow с указанным названием 
# если эксперимент с таким именем уже существует, 
# MLflow возвращает идентификатор существующего эксперимента
experiment = mlflow.get_experiment_by_name(EXPERIMENT_NAME)
if experiment is not None:
    experiment_id = experiment.experiment_id
else:
    experiment_id = mlflow.create_experiment(EXPERIMENT_NAME)


    
    
with mlflow.start_run(experiment_id=experiment_id, run_name=RUN_NAME) as run:
    # получаем уникальный идентификатор запуска эксперимента
    run_id = run.info.run_id
    
    # логируем метрики эксперимента
    # предполагается, что переменная stats содержит словарь с метриками,
    # где ключи — это названия метрик, а значения — числовые значения метрик
    mlflow.log_metrics(stats)

    # Логируем файлы в поддиректорию 'dataframe' внутри артефактов
    mlflow.log_artifact("columns.txt", artifact_path="dataframe")
    mlflow.log_artifact("users_churn.csv", artifact_path="dataframe")


experiment = mlflow.get_experiment_by_name(EXPERIMENT_NAME)
# получаем данные о запуске эксперимента по его уникальному идентификатору
run = mlflow.get_run(run_id)


# проверяем, что статус запуска эксперимента изменён на 'FINISHED'
# это утверждение (assert) можно использовать для автоматической проверки того, 
# что эксперимент был завершён успешно
assert run.info.status == "FINISHED"

# удаляем файлы 'columns.txt' и 'users_churn.csv' из файловой системы,
# чтобы очистить рабочую среду после логирования артефактов
os.remove("columns.txt")
os.remove("users_churn.csv")