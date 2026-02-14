PORTNAME=	gcpbucketbrute
DISTVERSION=	17.6866bd2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A script to enumerate Google Storage buckets, determine what access you have to them, and determine if they can be privilege escalated.
WWW=		https://github.com/RhinoSecurityLabs/GCPBucketBrute

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-google-cloud-storage@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
