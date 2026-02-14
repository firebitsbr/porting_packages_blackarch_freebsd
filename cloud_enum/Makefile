PORTNAME=	cloud_enum
DISTVERSION=	0.7.r11.g13fefdb
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Multi-cloud OSINT tool. Enumerate public resources in AWS, Azure, and Google Cloud.
WWW=		https://github.com/initstring/cloud_enum

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-dnspython@${PY_FLAVOR} \
		??/py-requests-futures@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
