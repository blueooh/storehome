#!/bin/sh 

DEPLOY_PATH=$1
DEPLOY_FILES=('./intro' './static' './tastegood' './templates')
APACHE2_CONF_PATH="/etc/apache2/sites-available"
WEBAPP_SETTINGS_FILE="./deploy/settings.py"
APACHE2_CONF_FILE="./deploy/taste-good.com"

echo "deploy path is $DEPLOY_PATH"

if [ -d $DEPLOY_PATH ]; then
    echo "$DEPLOY_PATH already exists..."
    exit
else
    /etc/init.d/apache2 stop
    mkdir -p $DEPLOY_PATH
fi

for file in ${DEPLOY_FILES[@]}
do
    echo "copy $file to $DEPLOY_PATH"
    cp -r $file $DEPLOY_PATH
done

cp $WEBAPP_SETTINGS_FILE "$DEPLOY_PATH/tastegood"
cp $APACHE2_CONF_FILE $APACHE2_CONF_PATH

chown -R www-data $DEPLOY_PATH

a2ensite "taste-good.com"
/etc/init.d/apache2 restart
