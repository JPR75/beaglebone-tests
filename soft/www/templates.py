#!/usr/bin/env python
# -*- coding: utf-8 -*-

admin_html = """
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

  <body>
    <h2>Admin</h2>
    <p>
      {}<br />
      {}
    </p>
    <p>
      Free RAM : {} MB
    </p>
    <p>
      Processor : {} ; {}<br />
      OS : {}<br />
      Vesrion : {}<br />
      Python : {}<br />
      I am : {}
    </p>
    <hr />
    <form method="get" action="admin.wsgi">
      <img class="centred" src="img/danger.png" />
      <p>
        Admin password : <input type="password" name="pwd">
      </p>
      <p>
        <input name="admin_action" type="radio" value="reboot"> Reboot<br />
        <input name="admin_action" type="radio" value="shut_down"> Shut down
      </p>
      <p>
        <input type="submit" value="Submit">
      </p>
    </form>
    <p>
      pwd : {}<br />
      action : {}
    </p>
    <hr />
    <p class="centred">
      <a href="javascript:self.close();"> > close window < </a>
    </p>
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

  <body>
    <h2>Setting</h2>
    <p class="slight">
      &Delta;&Phi; = {}
    </p>
    <form method="get" action="cmd.wsgi">
      <p>
        Enter &Delta;&Phi; : <input type="text" name="delta" value="{}">
      </p>
      <p>
        <input type="submit" value="Submit">
      </p>
    </form>
  </body>
</html>"""

data_html = """
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

  <body>
    <h2>Data</h2>
    <p class="emphase">
      &Delta;&Phi; = {}
    </p>
    <p class="emphase">
      Amp = {}
    </p>
    <p class="emphase">
      T&deg;C = {}
    </p>
  </body>
</html>"""

index_html = """
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

  <frameset rows="10%, 50%, 40%", class="home blog">
    <frame src="title.wsgi" name="title">
    <frameset cols="65%, 35%", class="home blog">
      <frame src="data.wsgi" name="data">
      <frame src="status.wsgi" name="status">
    </frameset>
    <frameset cols="65%, 35%", class="home blog">
      <frame src="cmd.wsgi" name="cmd">
      <frame src="info.wsgi" name="info">
    </frameset>
  </frameset>
</html>"""

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

  <body>
    <h2>Info</h2>
    <p class="centred">
      <a href="#" onclick="Popup=window.open('help.html','Popup','toolbar=no, location=no,status=no,menubar=no,scrollbars=yes,resizable=yes,width=420,height=400'); return false;">   &gt; Help &lt; </a>
    </p>
    <p class="centred">
      <a href="#" onclick="Popup=window.open('admin.wsgi','Popup','toolbar=no, location=no,status=no,menubar=no,scrollbars=yes,resizable=yes,width=420,height=600'); return false;">  &gt; Admin &lt; </a>
    </p>
  </body>
</html>"""

status_html = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en-US">

  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>BeagleBone Test</title>
    <meta name="description" content="BeagleBone Test">
    <meta name="keywords"content="BeagleBone Test">
    <meta name="identifier-URL" content="http://www.microreflexion.com">
    <meta http-equiv="refresh" content="3" />

    <link rel="stylesheet" href="style.css" type="text/css" media="screen" />
  </head>

  <body>
    <h2>Status</h2>
    <p>
      <img class="centred" src="img/{}" />
    </p>
    <p class="slight">
      {}
    </p>
    <p>
      {}
    </p>
  </body>
</html>"""

title_html = """
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

  <body>
    <h1>Beaglebone Test</h1>
  </body>
</html>"""
