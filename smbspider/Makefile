PORTNAME=	smbspider
DISTVERSION=	10.7db9323
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A lightweight python utility for searching SMB/CIFS/Samba file shares.
WWW=		https://github.com/T-S-A/smbspider

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-netaddr@${PY_FLAVOR} \
		??/py-pysmb@${PY_FLAVOR} \
		??/py-pysmbc@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
