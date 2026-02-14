PORTNAME=	quickrecon
DISTVERSION=	0.3.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A python script for simple information gathering. It attempts to find subdomain names, perform zone transfers and gathers emails from Google and Bing.
WWW=		http://packetstormsecurity.com/files/104314/QuickRecon-0.3.2.html

LICENSE=	GPLv3 # Defaulting to GPLv3


RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-html5lib@${PY_FLAVOR} \
		??/py-httplib2@${PY_FLAVOR} \
		??/py-pyqt4@${PY_FLAVOR} \
		??/py-sip@${PY_FLAVOR} \
		??/pyqt4-common \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
