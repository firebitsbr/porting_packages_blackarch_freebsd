PORTNAME=	weirdaal
DISTVERSION=	331.c14e36d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	AWS Attack Library.
WWW=		https://github.com/carnal0wnage/weirdAAL

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-boto3@${PY_FLAVOR} \
		??/py-botocore@${PY_FLAVOR} \
		??/py-dateutil@${PY_FLAVOR} \
		??/py-docutils@${PY_FLAVOR} \
		??/py-jmespath@${PY_FLAVOR} \
		??/py-s3transfer@${PY_FLAVOR} \
		??/py-tabulate@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
