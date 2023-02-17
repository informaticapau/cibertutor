import click
import yaml
from flask.cli import AppGroup
from os import listdir, environ
from os.path import isfile, join
from markdown import markdown
from flaskapp.utils import db
from ..models.module import ModuleRep
from ..models.topic import TopicRep
from ..models.theory import TheoryRep
from ..models.practice import PracticeRep
from ..models.answers import AnswersRep

db_cli = AppGroup('db', short_help="Courses' Data Base options.")

@db_cli.command('load')
@click.option('-d', '--debug', is_flag=True, help ='Activates DEBUG mode.')
def load_data(debug):
    """Loads data from YAML files."""    
    
    def get_data_dir() -> str:
        return environ['MODULES_DATA_FOLDER']


    def get_data_files(data_dir: str = get_data_dir()) -> list[str]:
        click.echo(f'Reading data in {data_dir}...')

        files: list[str] = []

        try:
            data: list[str] = listdir(data_dir)
        except:
            print(f'Error listing data files in dir {data_dir}.')
        else:
            data: list[str] = [d for d in data if not d.startswith('.')]
            for file in data:
                file_path = join(data_dir, file)
                if isfile(file_path) and file.endswith(('.yaml', '.yml')):
                    files.append(file_path)

        return files


    def read_file(file: str) -> dict:
        with open(file, 'r') as f:
            return yaml.safe_load(f)
        
    try:
        for file in get_data_files():
            
            if file.startswith('.'):
                pass
            print(f'Extracting data from: {file}')
            
            data: dict = read_file(file)
            if debug: click.echo(data)

            if debug: click.echo(f"Reading Module: {data['title']}")
            m = ModuleRep(
                title = data['title'],
                description = markdown(data['description']),
                ordinal = data['ordinal'],
                icon = data.get('icon')
            )
            db.session.add(m)

            module_id = ModuleRep.query\
                .filter(ModuleRep.title == data['title'])\
                .first().id

            for topic in data['topics']:
                if debug:
                    click.echo('\t' + f"Topic: {topic['title']}")
                t = TopicRep(
                    title = topic['title'],
                    description = markdown(topic['description']),
                    module = module_id,
                    ordinal = topic['ordinal']
                )
                db.session.add(t)
                
                topic_id = TopicRep.query\
                .filter(TopicRep.title == topic['title'])\
                .first().id

                for theory in topic['lessons']:
                    if debug:
                        click.echo('\t'*2 + f"Lesson: {theory['title']}")
                    th = TheoryRep(
                        title = theory['title'],
                        content = markdown(theory['content'])
                            .replace('\n', '</p>\n\t<p>'),
                        topic = topic_id,
                        ordinal = theory['ordinal']
                    )
                    db.session.add(th)

                if topic.get('exercises') is not None:
                    for practice in topic['exercises']:
                        if debug:
                            click.echo('\t'*2
                                       + f"Exercise: {practice['title']}")
                        pr = PracticeRep(
                            title = practice['title'],
                            content = markdown(practice['content']),
                            style = practice['style'],
                            topic = topic_id,
                            ordinal = practice['ordinal']
                        )
                        db.session.add(pr)
                        
                        practice_id = PracticeRep.query\
                            .filter(PracticeRep.topic == topic_id,
                                    PracticeRep.title == practice['title'])\
                            .first().id
                        
                        answer_id: int = 0
                        for answer in practice['answers']:
                            answer_id += 1
                            a = AnswersRep(
                                practice = practice_id,
                                id = answer_id,
                                content = markdown(answer['content']),
                                is_solution = answer['is_solution']
                            )
                            db.session.add(a)

            click.echo(f"Module loaded: {data['title']}")
        db.session.commit()
        click.echo(f"The changes were commited.")

    except Exception as e:
        click.echo('Error while loading data:')
        click.echo(e)
        db.session.rollback()

@db_cli.command('clear')
def clear_data():
    """Purges data from the Data Base without deleting the tables."""
    db.session.query(AnswersRep).delete()
    db.session.query(PracticeRep).delete()
    db.session.query(TheoryRep).delete()
    db.session.query(TopicRep).delete()
    db.session.query(ModuleRep).delete()
    db.session.commit()
    click.echo('The data base was cleared.')