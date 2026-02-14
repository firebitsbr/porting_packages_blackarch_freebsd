PORTNAME=	faradaysec
DISTVERSION=	v3.19.0.r2583.g77edf29
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Collaborative Penetration Test and Vulnerability Management Platform.
WWW=		http://www.faradaysec.com/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/couchdb \
		??/gobject-introspection \
		??/gobject-introspection-runtime \
		??/gtk3 \
		??/java-environment \
		??/libpqxx \
		??/postgresql \
		??/py-alembic@${PY_FLAVOR} \
		??/py-anyascii@${PY_FLAVOR} \
		??/py-apispec-webframeworks@${PY_FLAVOR} \
		??/py-apispec@${PY_FLAVOR} \
		??/py-autobahn@${PY_FLAVOR} \
		??/py-bcrypt@${PY_FLAVOR} \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-click@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-couchdb@${PY_FLAVOR} \
		??/py-dateutil@${PY_FLAVOR} \
		??/py-deprecation@${PY_FLAVOR} \
		??/py-distro@${PY_FLAVOR} \
		??/py-email-validator@${PY_FLAVOR} \
		??/py-faraday-plugins@${PY_FLAVOR} \
		??/py-filedepot@${PY_FLAVOR} \
		??/py-filteralchemy-fork@${PY_FLAVOR} \
		??/py-flask-classful@${PY_FLAVOR} \
		??/py-flask-kvsession-fork@${PY_FLAVOR} \
		??/py-flask-login@${PY_FLAVOR} \
		??/py-flask-restless@${PY_FLAVOR} \
		??/py-flask-security@${PY_FLAVOR} \
		??/py-flask-sqlalchemy@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-gobject@${PY_FLAVOR} \
		??/py-hypothesis@${PY_FLAVOR} \
		??/py-ipy@${PY_FLAVOR} \
		??/py-itsdangerous@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-marshmallow-sqlalchemy@${PY_FLAVOR} \
		??/py-marshmallow@${PY_FLAVOR} \
		??/py-mockito@${PY_FLAVOR} \
		??/py-msgpack@${PY_FLAVOR} \
		??/py-nplusone@${PY_FLAVOR} \
		??/py-pendulum@${PY_FLAVOR} \
		??/py-pgcli@${PY_FLAVOR} \
		??/py-pillow@${PY_FLAVOR} \
		??/py-prompt_toolkit@${PY_FLAVOR} \
		??/py-psycopg2@${PY_FLAVOR} \
		??/py-pyasn1@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-pysqlite3@${PY_FLAVOR} \
		??/py-pytest@${PY_FLAVOR} \
		??/py-pytz@${PY_FLAVOR} \
		??/py-responses@${PY_FLAVOR} \
		??/py-selenium@${PY_FLAVOR} \
		??/py-service-identity@${PY_FLAVOR} \
		??/py-shodan@${PY_FLAVOR} \
		??/py-simplejson@${PY_FLAVOR} \
		??/py-simplekv@${PY_FLAVOR} \
		??/py-slugify@${PY_FLAVOR} \
		??/py-sphinx@${PY_FLAVOR} \
		??/py-sqlalchemy@${PY_FLAVOR} \
		??/py-syslog-rfc5424-formatter@${PY_FLAVOR} \
		??/py-tornado@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		??/py-twisted@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		??/py-w3af-api-client@${PY_FLAVOR} \
		??/py-webargs@${PY_FLAVOR} \
		??/py-websocket-client@${PY_FLAVOR} \
		??/py-werkzeug@${PY_FLAVOR} \
		??/py-whoosh@${PY_FLAVOR} \
		??/py-wtforms@${PY_FLAVOR} \
		??/pyqt3 \
		??/vte3 \
		??/zsh \
		devel/py-pip@${PY_FLAVOR} \
		ftp/curl \
		lang/python \
		lang/ruby \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
