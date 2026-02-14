PORTNAME=	kerberoast
DISTVERSION=	0.2.0.r9.g82f5bb2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Kerberoast attack -pure python-.
WWW=		https://github.com/skelsec/kerberoast

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-asyauth@${PY_FLAVOR} \
		??/py-minikerberos@${PY_FLAVOR} \
		??/py-msldap@${PY_FLAVOR} \
		??/py-unicrypto@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
