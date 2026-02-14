PORTNAME=	pkinittools
DISTVERSION=	13.0f0cfa5
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Tools for Kerberos PKINIT and relaying to AD CS.
WWW=		https://github.com/dirkjanm/PKINITtools

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/impacket \
		??/py-asysocks@${PY_FLAVOR} \
		??/py-minikerberos@${PY_FLAVOR} \
		??/py-oscrypto@${PY_FLAVOR} \
		??/py-pyasn1@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
