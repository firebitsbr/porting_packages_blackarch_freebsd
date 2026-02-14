PORTNAME=	hiddeneye
DISTVERSION=	1228.7a3deaf
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Modern phishing tool with advanced functionality.
WWW=		https://github.com/DarkSecDevelopers/HiddenEye

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-future@${PY_FLAVOR} \
		??/py-pgrep@${PY_FLAVOR} \
		??/py-pyngrok@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		lang/php82 \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
