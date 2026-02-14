PORTNAME=	drozer
DISTVERSION=	2.4.4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A security testing framework for Android - Precompiled binary from official repository.
WWW=		https://github.com/mwrlabs/drozer

LICENSE=	GPLv3 # Defaulting to GPLv3


RUN_DEPENDS=	??/jre8-openjdk \
		??/protobuf \
		??/py-protobuf@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-service-identity@${PY_FLAVOR} \
		??/py-twistedx@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
