PORTNAME=	enumerate-iam
DISTVERSION=	14.4529114
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Enumerate the permissions associated with an AWS credential set.
WWW=		https://github.com/andresriancho/enumerate-iam

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-boto3@${PY_FLAVOR} \
		??/py-botocore@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
