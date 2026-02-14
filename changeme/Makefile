PORTNAME=	changeme
DISTVERSION=	272.26fa2c3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A default credential scanner.
WWW=		https://github.com/ztgrace/changeme

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-cerberus@${PY_FLAVOR} \
		??/py-jinja@${PY_FLAVOR} \
		??/py-libnmap@${PY_FLAVOR} \
		??/py-logutils@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-memcached@${PY_FLAVOR} \
		??/py-mock@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		??/py-nose@${PY_FLAVOR} \
		??/py-paramiko@${PY_FLAVOR} \
		??/py-pymongo@${PY_FLAVOR} \
		??/py-pyodbc@${PY_FLAVOR} \
		??/py-pysnmp@${PY_FLAVOR} \
		??/py-redis@${PY_FLAVOR} \
		??/py-schema@${PY_FLAVOR} \
		??/py-selenium@${PY_FLAVOR} \
		??/py-shodan@${PY_FLAVOR} \
		??/py-sqlalchemy@${PY_FLAVOR} \
		??/py-tabulate@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
