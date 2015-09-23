# coding: utf-8

import luigi

class TemplateTask(luigi.Task):

    # Parámetro
    report_date = luigi.DateParameter()

    def requires(self):
        """
        ¿Qué otra tarea debe de estar completada antes de que esta clase inicie?
        """
        return [MyUpstreamTask(self.report_date)]

    def output(self):
        """
        Cuándo esta tarea esté completada, ¿Qué debe de producir como salida?
        Esta salida determina si va a ejecutarse o no la tarea
        """
        return S3Target('s3://my-output-bucket/my-example-tasks-output')

    def run(self):
        """
        Luisgi mandar a ejecutar esta función, si la tarea debe de ejecutarse
        """
        ## Podemos ejecutar casi cualquier código aquí
