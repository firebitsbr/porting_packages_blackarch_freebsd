PORTNAME=	scout2
DISTVERSION=	1182.5d86d46
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Security auditing tool for AWS environments.
WWW=		http://isecpartners.github.io/Scout2/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-boto3@${PY_FLAVOR} \
		??/py-botocore@${PY_FLAVOR} \
		??/py-dateutil@${PY_FLAVOR} \
		??/py-iampoliciesgonewild@${PY_FLAVOR} \
		??/py-jmespath@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		??/py-opinel@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
