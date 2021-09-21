from app import create_app, db
from app.models import User, Pitch
from flask_script import Manager,Server

#creating app instance
app = create_app('development')

manager = Manager(app)

manager.add_command('server', Server)

@manager.command
def test():
    '''
    Run unit tests
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():

    db.create_all()
    return dict(app = app,db = db,User = User, Pitch = Pitch )


if __name__ == '__main__':
    manager.run()