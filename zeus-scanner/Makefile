PORTNAME=	zeus-scanner
DISTVERSION=	414.21b8756
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Advanced dork searching utility.
WWW=		https://github.com/Ekultek/Zeus-Scanner

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-nmap@${PY_FLAVOR} \
		??/py-psutil@${PY_FLAVOR} \
		??/py-pyvirtualdisplay@${PY_FLAVOR} \
		??/py-selenium@${PY_FLAVOR} \
		??/py-whichcraft@${PY_FLAVOR} \
		lang/python \
		security/nmap \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
