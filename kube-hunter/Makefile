PORTNAME=	kube-hunter
DISTVERSION=	703.bc47f08
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Hunt for security weaknesses in Kubernetes clusters.
WWW=		https://github.com/aquasecurity/kube-hunter

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-future@${PY_FLAVOR} \
		??/py-kubernetes@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		??/py-netifaces@${PY_FLAVOR} \
		??/py-packaging@${PY_FLAVOR} \
		??/py-pluggy@${PY_FLAVOR} \
		??/py-prettytable@${PY_FLAVOR} \
		??/py-ruamel-yaml@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		lang/python \
		net/py-scapy@${PY_FLAVOR} \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
