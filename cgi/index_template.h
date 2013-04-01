char header_text[] =  "Content-Type: text/html\n\n \
<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">\n \
  <html xmlns=\"http://www.w3.org/1999/xhtml\" lang=\"en-US\">\n\n \
  <head>\n \
    <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\" />\n \
    <title>BeagleBone Test</title>\n \
    <meta name=\"description\" content=\"BeagleBone Test\">\n \
    <meta name=\"keywords\"content=\"BeagleBone Test\">\n \
    <meta name=\"identifier-URL\" content=\"http://www.microreflexion.com\">\n \
    <meta http-equiv=\"refresh\" content=\"1\" />\n\n \
    <link rel=\"stylesheet\" href=\"style.css\" type=\"text/css\" media=\"screen\" />\n \
  </head>\n\n \
  <body class=\"home blog\">\n \
    <p>\n \
      <a href=\"./index.wsgi\">Home</a> | <a href=\"./cmd.wsgi\">Cmd</a> | <a href=\"./info.wsgi\">Info</a>\n \
    </p>\n \
    <br />\n \
    <p>\n";

char footer_text[] =" \
    </p>\n \
    <br />\n \
   </body>\n \
  </html>\n";

char body_text[] = "Hello %s !!!\n";
