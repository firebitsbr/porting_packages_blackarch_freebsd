PORTNAME=	smbclient-ng
DISTVERSION=	3.0.0.r0.gf03303f
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Interact with SMB shares.
WWW=		https://github.com/p0dalirius/smbclient-ng

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/impacket-ba \
		??/py-charset-normalizer@${PY_FLAVOR} \
		??/py-pefile@${PY_FLAVOR} \
		??/py-rich@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
