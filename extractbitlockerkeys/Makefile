PORTNAME=	extractbitlockerkeys
DISTVERSION=	1.2.r20.g54730e4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Script to automatically extract the bitlocker recovery keys from a domain.
WWW=		https://github.com/p0dalirius/extractbitlockerkeys

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-sectools@${PY_FLAVOR} \
		??/py-xlsxwriter@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
