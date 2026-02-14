PORTNAME=	sqlivulscan
DISTVERSION=	249.cc8e657
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	This will give you the SQLi Vulnerable Website Just by Adding the Dork.
WWW=		https://github.com/Hadesy2k/sqlivulscan

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-nyawc@${PY_FLAVOR} \
		??/py-simplejson@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		??/py-terminaltables@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
