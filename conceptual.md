### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  Python is an OOP language. JS is a frontend language

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing. 

    dictonary.get("c")
    if "c" in list(dictionary.keys()):
      return True
    else:
      return False 
- What is a unit test?
  A test for functionality in a single piece of code

- What is an integration test?
  A test to see if parts of an application are functioning together

- What is the role of web application framework, like Flask?
  To make building apps easier and faster, to have a sessions, and authentication feature

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  'foods/pretzel' seems more for an entire topic while 'foods?type=pretzel' seems more like a query string through a search

- How do you collect data from a URL placeholder parameter using Flask?
   in the URL object you must get the "name" for the object

- How do you collect data from the query string using Flask?
   request.args[""] 

- How do you collect data from the body of the request using Flask?
   request.form  

- What is a cookie and what kinds of things are they commonly used for?
  cookie is saved bits of data that is stored client or server side that gets sent with http requests. 

- What is the session object in Flask?
  The session object is a codified cookie object that contains all the stored cookies in the browser session. It can not be modified and is in code.

- What does Flask's `jsonify()` do?
  jsonify turns a data object into json which is a dictionary.
