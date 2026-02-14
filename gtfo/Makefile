PORTNAME=	gtfo
DISTVERSION=	17.873d862
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Search gtfobins and lolbas files from your terminal.
WWW=		https://github.com/mzfr/gtfo

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-pyaml@${PY_FLAVOR} \
		??/py-pyfiglet@${PY_FLAVOR} \
		??/py-requests-cache@${PY_FLAVOR} \
		??/py-tabulate@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
