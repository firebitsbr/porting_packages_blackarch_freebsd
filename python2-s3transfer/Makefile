PORTNAME=	python2-s3transfer
DISTVERSION=	0.2.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An Amazon S3 Transfer Manager.
WWW=		https://pypi.org/project/s3transfer/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-botocore@${PY_FLAVOR} \
		??/py-futures@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
