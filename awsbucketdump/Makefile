PORTNAME=	awsbucketdump
DISTVERSION=	82.4684670
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tool to quickly enumerate AWS S3 buckets to look for loot.
WWW=		https://github.com/jordanpotti/AWSBucketDump

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-xmltodict@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
