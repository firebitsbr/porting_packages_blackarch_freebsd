PORTNAME=	smalisca
DISTVERSION=	58.1aa7a16
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Static Code Analysis for Smali files.
WWW=		https://github.com/dorneanu/smalisca

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/graphviz \
		??/py-cement@${PY_FLAVOR} \
		??/py-configparser@${PY_FLAVOR} \
		??/py-flask-restless@${PY_FLAVOR} \
		??/py-flask-sqlalchemy@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-mimerender@${PY_FLAVOR} \
		??/py-prettytable@${PY_FLAVOR} \
		??/py-pyfiglet@${PY_FLAVOR} \
		??/py-pygraphviz@${PY_FLAVOR} \
		??/py-sqlalchemy@${PY_FLAVOR} \
		??/py-werkzeug@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
