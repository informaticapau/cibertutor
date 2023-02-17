blueprints: list = []

try:
    from .home import bp
    blueprints.append(bp)
except Exception as e:
    print('Could not import blueprint "home"')
    print(e)

try:
    from .courses import bp
    blueprints.append(bp)
    from .courses.utils.api import bp
    blueprints.append(bp)
except Exception as e:
    print('Could not import blueprint "courses"')
    print(e)

try:
    from .tools.phishing_quiz import bp
    blueprints.append(bp)
    from .tools.phishing_quiz.utils.api import bp
    blueprints.append(bp)
except Exception as e:
    print('Could not import blueprint "phishing_quiz"')
    print(e)
    
try:
    from .tools.password_checker import bp
    blueprints.append(bp)
except Exception as e:
    print('Could not import blueprint "password_checker"')
    print(e)

try:
    from .tools import bp
    blueprints.append(bp)
except Exception as e:
    print('Could not import blueprint "tools"')
    print(e)

