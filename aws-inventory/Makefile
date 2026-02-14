PORTNAME=	aws-inventory
DISTVERSION=	19.9a2fa8e
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Discover resources created in an AWS account.
WWW=		https://github.com/nccgroup/aws-inventory

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-argparse@${PY_FLAVOR} \
		??/py-botocore@${PY_FLAVOR} \
		??/py-opinel@${PY_FLAVOR} \
		??/tk \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
