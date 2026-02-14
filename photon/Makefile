PORTNAME=	photon
DISTVERSION=	v1.2.2.r45.g4b9b451
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Incredibly fast crawler which extracts urls, emails, files, website accounts and much more.
WWW=		https://github.com/s0md3v/Photon

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-tld@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
