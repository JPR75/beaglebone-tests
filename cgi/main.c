#include <stdio.h>
#include <stdlib.h>

#include "index_template.h"

void header (void) {
  printf("%s", header_text);
}

void footer (void) {
  printf("%s", footer_text);
}

void body (char *text) {
  printf(body_text, text);
}

int main (void) {
  header ();
  body ("world");
  footer ();
  return 0;
}

