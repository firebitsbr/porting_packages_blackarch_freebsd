PORTNAME=	python-msldap
DISTVERSION=	0.5.15
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python library to play with MS LDAP.
WWW=		https://github.com/skelsec/msldap

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-asn1crypto@${PY_FLAVOR} \
		??/py-asyauth@${PY_FLAVOR} \
		??/py-asysocks@${PY_FLAVOR} \
		??/py-prompt_toolkit@${PY_FLAVOR} \
		??/py-tabulate@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		??/py-unicrypto@${PY_FLAVOR} \
		??/py-wcwidth@${PY_FLAVOR} \
		??/py-winacl@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
