import datetime
from typing import Optional, Union, Dict, List

import ormar
from src.config.settings import metadata, database


class Category(ormar.Model):
    """ Categories by project
    """
    class Meta:
        metadata = metadata
        database = database

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=150)
    # parent: Optional['Category'] = ormar.ForeignKey(
    #     'Category', related_name="children", nullable=True
    # )


class Toolkit(ormar.Model):
    """ Toolkit by project
    """
    class Meta:
        metadata = metadata
        database = database

    id: int = ormar.Integer(primary_key=True)
    name = ormar.String(max_length=150)
    # parent = ormar.ForeignKey('self', related_name="children", nullable=True)


class Team(ormar.Model):
    class Meta:
        metadata = metadata
        database = database

    id: int = ormar.Integer(primary_key=True)
    name = ormar.String(max_length=150)


class ProjectTeam(ormar.Model):
    class Meta:
        tablename = "project_teams"
        database = database
        metadata = metadata


class Project(ormar.Model):
    """ Model project
    """
    class Meta:
        metadata = metadata
        database = database

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=150)
    description: str = ormar.Text()
    create_date: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    category: Optional[Union[Category, Dict]] = ormar.ForeignKey(
        Category, related_name="projects", name='category_id'
    )
    toolkit: Optional[Union[Toolkit, Dict]] = ormar.ForeignKey(
        Toolkit, related_name="projects", name='toolkit_id'
    )
    team: Optional[Union[Team, List[Team]]] = ormar.ManyToMany(
        Team, related_name='projects', through=ProjectTeam
    )




# class Repository(models.Model):
#     repo_id = fields.IntField()
#     created_at = fields.DatetimeField()
#     updated_at = fields.DatetimeField()
#     stars = fields.IntField()
#     forks = fields.IntField()
#     watch = fields.IntField()
#     topics = fields.CharField(max_length=1000)
#     languages = fields.CharField(max_length=1000)
#     description = fields.CharField(max_length=1000)
#
#
# class Task(models.Model):
#     """ Model task by project
#     """
#     description = fields.TextField()
#     create_date = fields.DatetimeField(auto_now_add=True)
#     start_date = fields.DatetimeField(null=True)
#     end_date = fields.DatetimeField(null=True)
#     project = fields.ForeignKeyField('models.Project', related_name='tasks')
#     worker = fields.ForeignKeyField('models.User', related_name='tasks', null=True)
#
#
# class CommentTask(models.Model):
#     """ Model comment by task
#     """
#     user = fields.ForeignKeyField('models.User', related_name='task_comments')
#     task = fields.ForeignKeyField('models.Task', related_name='comments')
#     message = fields.CharField(max_length=1000)
#     create_date = fields.DatetimeField(auto_now_add=True)
