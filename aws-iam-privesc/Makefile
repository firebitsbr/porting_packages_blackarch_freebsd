PORTNAME=	aws-iam-privesc
DISTVERSION=	11.2983efd
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	AWS IAM policy scanner that helps determine where privilege escalation can be achieved.
WWW=		https://github.com/cyberqueenmeg/aws_iam_privesc

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/aws-cli \
		??/py-boto3@${PY_FLAVOR} \
		??/py-botocore@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
