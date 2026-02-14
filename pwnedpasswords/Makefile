PORTNAME=	pwnedpasswords
DISTVERSION=	3.0.0.r7.ge33d4bb
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Generate and verify pwnedpasswords check digits.
WWW=		https://github.com/lionheart/pwnedpasswords

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-future@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
