PORTNAME=	dirhunt
DISTVERSION=	329.a5ea20d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Find web directories without bruteforce.
WWW=		https://github.com/hahwul/dirhunt

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-click@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-google@${PY_FLAVOR} \
		??/py-humanize@${PY_FLAVOR} \
		??/py-legacy-cgi@${PY_FLAVOR} \
		??/py-proxy-db@${PY_FLAVOR} \
		??/py-requests-mock@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
