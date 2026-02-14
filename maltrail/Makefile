PORTNAME=	maltrail
DISTVERSION=	1.1.r336.g736a430
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Malicious traffic detection system.
WWW=		https://github.com/stamparm/maltrail

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-pcapy@${PY_FLAVOR} \
		??/py-pysqlite3@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
