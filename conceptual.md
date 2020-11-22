### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

  1. Python has procedural programming while JavaScript does not
  2. JavaScript can be used to power front and back end development while Python is primarily only a backend language
  3. Python is designed to be future proof while JavaScript has yearly updates that may break some code's functionality
  4. JavaScript runs faster than Python
  5. Python has no way of inheriting instances, unlike the functionality of JavaScript
  6. Python has many different numeric types (i.e. float, int, fixed-point decimal, etc.) while JavaScript only uses floating point numbers
  7. Syntax differs heavily–Python uses indentations and JavaScript uses curly braces

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

  1. Use the dictionary `get()` method: `dict.get(keyname, value)`
  2. Use the dictionary `setdefault()` method: `dict.setdefault(keyname, value)`

- What is a unit test?

  - Tests an individual component

- What is an integration test?

  - Tests that multiple parts work together

- What is the role of web application framework, like Flask?

  - A web framework, like Flask, is used to build and deploy web apps to a server. It can interpret APIs, web resources, and other related services. 

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  - It really just depends. For example, you would use a route URL in a RESTful API. You would use a route URL when trying to identify a resource, but when you want to sort or filter through some sort of dictionary or list you would use a URL query parameter.
  
- How do you collect data from a URL placeholder parameter using Flask?

  ``` python
  from flask import request
  
  @app.route("/where-to/<id>")
  def where_to(id):
    url_for("where-to", id="here")
    
  # /where-to/here
  ```

- How do you collect data from the query string using Flask?

  ``` python
  from flask import request
  
  @app.route("/where-to", methods=["GET"])
  def where_to():
    return request.query_string
  ```

- How do you collect data from the body of the request using Flask?

  ``` python
  from flask import request
  
  @app.route("/home", methods=["GET"])
  def home():
    body = request.form.get("body")
  ```

- What is a cookie and what kinds of things are they commonly used for?

  - Cookies are small files stored in a user's browser. They store information like a username or password. There are two types, persistent and session cookies. 

- What is the session object in Flask?

  - A session object in Flask is used to track session data. It is a dictionary type that contains a key value pair of the session variables and their values. 

- What does Flask's `jsonify()` do?

  - It turns JSON output into a response object, such as an array or mulriple keywork arguments into a dictionary.
