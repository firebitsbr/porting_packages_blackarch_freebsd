PORTNAME=	sooty
DISTVERSION=	335.6236fd1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	The SOC Analysts all-in-one CLI tool to automate and speed up workflow.
WWW=		https://github.com/TheresAFewConors/Sooty

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-asn1crypto@${PY_FLAVOR} \
		??/py-certifi@${PY_FLAVOR} \
		??/py-cffi@${PY_FLAVOR} \
		??/py-chardet@${PY_FLAVOR} \
		??/py-cryptography@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-idna@${PY_FLAVOR} \
		??/py-ipwhois@${PY_FLAVOR} \
		??/py-pycparser@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-pysocks@${PY_FLAVOR} \
		??/py-strictyaml@${PY_FLAVOR} \
		??/py-unfurl@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		??/py-wget@${PY_FLAVOR} \
		??/py-win_inet_pton@${PY_FLAVOR} \
		??/py-wincertstore@${PY_FLAVOR} \
		??/tk \
		devel/py-six@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
