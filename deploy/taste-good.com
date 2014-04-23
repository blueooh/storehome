<VirtualHost *:80>
	ServerAdmin bueooh@gmail.com
    DocumentRoot /data/www.taste-good.com/templates

    Alias /static/ /data/www.taste-good.com/static/

	<Directory /data/www.taste-good.com/tastegood>
        Order deny,allow
        Allow from all
    </Directory>

    WSGIScriptAlias / /data/www.taste-good.com/tastegood/wsgi.py

	<Directory /data/www.taste-good.com/tastegood>
        <Files wsgi.py>
		    Order deny,allow
		    Allow from all
        </Files>
	</Directory>

	ErrorLog /home/blueooh/error.log

	LogLevel warn

</VirtualHost>
