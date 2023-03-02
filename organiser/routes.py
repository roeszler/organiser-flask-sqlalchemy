from flask import render_template, request, redirect, url_for
from organiser import app, db
from organiser.models import Category, Task, User # our custom classes


# ------------ create a basic app route using the root-level directory of slash
@app.route("/")
def home():
    tasks = list(Task.query.order_by(Task.id).all())
    # return render_template("base.html")
    return render_template("tasks.html", tasks=tasks)


@app.route("/categories")
def categories():
    # Query the 'Category' model, orderd by name, that is imported at the top of this file from:
    categories = list(Category.query.order_by(Category.category_name).all())

    # The first declaration of 'categories()' is the variable name that we can now use within the HTML template.
    # The second 'categories', which is now a list(), is the variable defined within our function
    # above, which is why, once again, it's important to keep your naming convention quite similar:
    # pass it into the rendered_template

    return render_template("categories.html", categories=categories)

# when a user eventually submits this form, the form will attempt to 'post' the
# data into the database, and this is why we need to specify both GET and POST
# methods in the app route. By default, the normal method is GET, so it will 
# behave as the 'else' condition since it's not part of the indented POST block:
# In real world model, consider adding defensive programming to handle brute-force 
# attacks, along with some error handling:

@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        # creates a new instance of the Category() model imported and why it's important 
        # to keep the naming convention consistent, which means our name-attribute matches 
        # that of our database model:
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):

    # a SQLAlchemy method called '.get_or_404()', which takes the argument of 'category_id'.
    # What this does is query the database and attempts to find the specified record using the data
    # provided, and if no match is found, it will trigger a 404 error page.

    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))


@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        task = Task(
            task_name=request.form.get("task_name"),
            task_description=request.form.get("task_description"),
            is_urgent=bool(True if request.form.get("is_urgent") else False),
            due_date=request.form.get("due_date"),
            category_id=request.form.get("category_id")
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_task.html", categories=categories)
    # in order for the dropdown list to route each available category, we need to 
    # pass that variable into the template. the first 'categories' listed is the 
    # variable name that we will be able to use on the template itself. The second 
    # 'categories' is simply the list of categories retrieved from the database defined above.


@app.route("/edit_task/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":

        # adding 'task dot' in front of each column-header, such as 'task.task_name', or 'task.due_date'.
        # It's important to do this for all fields, even if the user would only like to update one of them.
        # If we don't include all fields, and the user only updates the task_name for example, then
        # the other fields risk being deleted entirely.

        task.task_name = request.form.get("task_name")
        task.task_description = request.form.get("task_description")
        task.is_urgent = bool(True if request.form.get("is_urgent") else False)
        task.due_date = request.form.get("due_date")
        task.category_id = request.form.get("category_id")
        # db.session.add(task) # not needed as we are only modifying the specific task, no the task group
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit_task.html", task=task, categories=categories)


@app.route("/delete_task/<int:task_id>")
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        user = User(
            user_fname=request.form.get("user_fname"),
            user_lname=request.form.get("user_lname"),
            dob=request.form.get("dob"),
            user_email=request.form.get("user_email"),
            gender=request.form.get("gender"),
            profession=request.form.get("profession"),
            in_house=bool(True if request.form.get("in_house") else False),
            category_id=request.form.get("category_id")
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_user.html", categories=categories)


@app.route("/edit_user/<int:user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        user.user_fname = request.form.get("user_fname")
        user.user_lname = request.form.get("user_lname")
        user.dob = request.form.get("dob")
        user.user_email = request.form.get("user_email")
        user.gender = request.form.get("gender")
        user.profession = request.form.get("profession")
        task.is_urgent = bool(True if request.form.get("is_urgent") else False)
        task.category_id = request.form.get("category_id")
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit_user.html", user=user, task=task, categories=categories)


@app.route("/delete_user/<int:user_id>")
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("home"))