PORTNAME=	rsactftool
DISTVERSION=	1169.370cb43
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	RSA tool for ctf - retrieve private key from weak public key and/or uncipher data.
WWW=		https://github.com/Ganapati/RsaCtfTool

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-bitarray@${PY_FLAVOR} \
		??/py-cryptography@${PY_FLAVOR} \
		??/py-egcd@${PY_FLAVOR} \
		??/py-gmpy2@${PY_FLAVOR} \
		??/py-psutil@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/py-sympy@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		??/py-z3-solver@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
