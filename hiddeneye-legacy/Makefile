PORTNAME=	hiddeneye-legacy
DISTVERSION=	RC1.r226.g7a3deaf
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Modern Phishing Tool With Advanced Functionality.
WWW=		https://github.com/DarkSecDevelopers/HiddenEye-Legacy

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-certifi@${PY_FLAVOR} \
		??/py-chardet@${PY_FLAVOR} \
		??/py-future@${PY_FLAVOR} \
		??/py-idna@${PY_FLAVOR} \
		??/py-kill@${PY_FLAVOR} \
		??/py-pgrep@${PY_FLAVOR} \
		??/py-pyngrok@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
