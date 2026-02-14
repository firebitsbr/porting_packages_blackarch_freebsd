PORTNAME=	pmapper
DISTVERSION=	82.91d2e60
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tool for quickly evaluating IAM permissions in AWS.
WWW=		https://github.com/nccgroup/PMapper

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-botocore@${PY_FLAVOR} \
		??/py-dateutil@${PY_FLAVOR} \
		??/py-packaging@${PY_FLAVOR} \
		??/py-pydot@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
