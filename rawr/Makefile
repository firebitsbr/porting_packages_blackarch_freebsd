PORTNAME=	rawr
DISTVERSION=	74.544dd75
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Rapid Assessment of Web Resources. A web enumerator.
WWW=		https://bitbucket.org/al14s/rawr/wiki/Home

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/graphviz \
		??/phantomjs \
		??/py-imaging@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-pillow@${PY_FLAVOR} \
		??/py-pygraphviz@${PY_FLAVOR} \
		??/py-pyqt4@${PY_FLAVOR} \
		??/py-rdpy@${PY_FLAVOR} \
		??/py-xlsxwriter@${PY_FLAVOR} \
		lang/python3 \
		security/nmap


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
