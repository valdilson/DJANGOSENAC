from django.db import models

class Projeto(models.Model):
    titulo = models.CharField(
        verbose_name="Titulo do projeto ",
        max_length=30,
        help_text="titulo do projeto"
   )
    descricao = models.CharField(
        max_length=100,
        verbose_name="Descrição de projeto", help_text="descrição do projeto",
    )

    tecnologia = models.CharField(
        max_length=20,
        verbose_name="Tecnologia do projeto", help_text="Tecnologia do projeto",
    )

    class Meta:
        db_table: str = "projeto"
        verbose_name: str = "projeto"
        verbose_name_plural: str = "projetos"