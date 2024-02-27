from flask import Flask, render_template, redirect
from data import db_session
from data.models import User, Jobs
from forms.forms import RegisterForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    db_sess = db_session.create_session()
    data = db_sess.query(Jobs, User).filter(Jobs.team_leader == User.id)
    

    return render_template("index.html", title="Новости", data=data)

@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


def main():
    db_session.global_init("db/blogs.db")

    db_sess = db_session.create_session()

    # user = User(surname="Scott", name="Ridley",
    #             age=21, position="captain", 
    #             speciality="research engineer",
    #             address="module_1", email="scott_chief@mars.org")
    # db_sess.add(user)
    # user = User(surname="Takaev", name="Shamil",
    #             age=25, position="engineer",
    #             speciality="engineer",
    #             address="module_2", email="shamil@earth.org")
    # db_sess.add(user)
    # user = User(surname="Takaev", name="Adam",
    #             age=27, position="specialist",
    #             speciality="speciality",
    #             address="module_1", email="adam@neptun.org")
    # db_sess.add(user)
    # job = Jobs(team_leader=1, job="deployment of residental modules 1 and 2",
    #           work_size=15, collaborators="2, 3", is_finished=False)
    # db_sess.add(job)
    # db_sess.commit()
    # u = db_sess.query(User).filter(User.name=="Shamil").first()
    # job = Jobs(team_leader=u.id, job="Exploration of mineral resources", work_size=10,
    #            collaborators="4, 3", is_finished=False)
    # db_sess.add(job)
    # db_sess.commit()
    # u = db_sess.query(User).filter(User.name == "All").first()
    # user = db_sess.query(User).filter(User.id == 1).first()
    # news = News(title="Личная запись", content="Эта запись личная", 
    #             is_private=True)

    # db_sess.add(news)
    # db_sess.commit()
    app.run(debug=True)


if __name__ == '__main__':
    main()