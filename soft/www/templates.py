#!/usr/bin/env python

info_html = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en-US">

  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>BeagleBone Test</title>
    <meta name="description" content="BeagleBone Test">
    <meta name="keywords"content="BeagleBone Test">
    <meta name="identifier-URL" content="http://www.microreflexion.com">

    <link rel="stylesheet" href="style.css" type="text/css" media="screen" />
  </head>

  <body class="home blog">
    <p>
      <a href="./index.wsgi">Home</a> | <a href="./cmd.wsgi">Cmd</a> | <a href="./info.wsgi">Info</a>
    </p>
    <br />
    <p>
      Processor :  {} ; {}<br />
      OS            : {}<br />
      Vesrion    : {}<br />
      Python     : {}<br />
      I am : {}
    </p>
   </body>
</html>"""

home_html = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en-US">

  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>BeagleBone Test</title>
    <meta name="description" content="BeagleBone Test">
    <meta name="keywords"content="BeagleBone Test">
    <meta name="identifier-URL" content="http://www.microreflexion.com">
    <meta http-equiv="refresh" content="1" />

    <link rel="stylesheet" href="style.css" type="text/css" media="screen" />
  </head>

  <body class="home blog">
    <p>
      <a href="./index.wsgi">Home</a> | <a href="./cmd.wsgi">Cmd</a> | <a href="./info.wsgi">Info</a>
    </p>
    <br />
    <p>
      Phi = {}<br />
      Amp = {}<br />
      Temp = {}<br />
    </p>
    <br />
   </body>
</html>"""

cmd_html = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en-US">

  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>BeagleBone Test</title>
    <meta name="description" content="BeagleBone Test">
    <meta name="keywords"content="BeagleBone Test">
    <meta name="identifier-URL" content="http://www.microreflexion.com">

    <link rel="stylesheet" href="style.css" type="text/css" media="screen" />
  </head>

  <body class="home blog">
    <p>
      <a href="./index.wsgi">Home</a> | <a href="./cmd.wsgi">Cmd</a> | <a href="./info.wsgi">Info</a>
    </p>
    <br />
    <p>
      Delta = {}
    </p>
    <form method="get" action="cmd.wsgi">
      <p>
        Enter delta : <input type="text" name="delta">
      </p>
      <p>
        <input type="submit" value="Submit">
      </p>
    </form>
   </body>
</html>"""
