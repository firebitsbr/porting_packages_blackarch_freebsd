PORTNAME=	cybercrowl
DISTVERSION=	111.f7cac52
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Python Web path scanner tool.
WWW=		https://github.com/chamli/CyberCrowl

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-fake-useragent@${PY_FLAVOR} \
		??/py-idna@${PY_FLAVOR} \
		??/py-requests-file@${PY_FLAVOR} \
		??/py-requests-ntlm@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
