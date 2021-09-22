#!/bin/bash

# Program Name: user_response
# outputs the username the user inputted into
# the user.html form

# -1. Consider writing to a logfile
# 0. Consult a configuration file, .htaccess
# 1. consult the environments
# 2. optional read the HTTP body
# 3. emit my HTTP response header
# 4. emit a blank line
# 5. emit my HTTP response body

if [ -f ./.htaccess ] ; then
  source ./.htaccess
fi

echo "This program ran on: $(date)" >> ./user_response.log

# Read the value from user.html which was placed into the query string
USERNAME=${QUERY_STRING#*username=}
USERNAME=${USERNAME%%&*}
USERNAME=${USERNAME//+/ }

# emit my HTTP response header
echo "content-type: text/html"
echo "X-directory: $(pwd)"
echo "X-class: cit384"

# emit a blank line
echo ""

# emit my HTTP response body
cat <<EOF
<!DOCTYPE html>
<html>
<head>
<title>Username</title>
</head>
<body>
EOF

echo "<p> Username you entered: $USERNAME </p>"

# emit some of the HTML Stuff
cat <<EOF
</body>
</html>
EOF
