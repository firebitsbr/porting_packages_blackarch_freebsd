PORTNAME=	python-dissect.target
DISTVERSION=	3.24.r46.g6e90e30
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	The Dissect module tying all other Dissect modules together. It provides a programming API and command line tools which allow easy access to various data sources inside disk images or file collections (a.k.a. targets).
WWW=		https://github.com/fox-it/dissect.target

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-setuptools-scm@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/ipython \
		??/py-asn1crypto@${PY_FLAVOR} \
		??/py-defusedxml@${PY_FLAVOR} \
		??/py-dissect.archive@${PY_FLAVOR} \
		??/py-dissect.btrfs@${PY_FLAVOR} \
		??/py-dissect.cim@${PY_FLAVOR} \
		??/py-dissect.clfs@${PY_FLAVOR} \
		??/py-dissect.cstruct@${PY_FLAVOR} \
		??/py-dissect.esedb@${PY_FLAVOR} \
		??/py-dissect.etl@${PY_FLAVOR} \
		??/py-dissect.eventlog@${PY_FLAVOR} \
		??/py-dissect.evidence@${PY_FLAVOR} \
		??/py-dissect.extfs@${PY_FLAVOR} \
		??/py-dissect.fat@${PY_FLAVOR} \
		??/py-dissect.ffs@${PY_FLAVOR} \
		??/py-dissect.fve@${PY_FLAVOR} \
		??/py-dissect.hypervisor@${PY_FLAVOR} \
		??/py-dissect.jffs@${PY_FLAVOR} \
		??/py-dissect.ntfs@${PY_FLAVOR} \
		??/py-dissect.ole@${PY_FLAVOR} \
		??/py-dissect.regf@${PY_FLAVOR} \
		??/py-dissect.shellitem@${PY_FLAVOR} \
		??/py-dissect.sql@${PY_FLAVOR} \
		??/py-dissect.squashfs@${PY_FLAVOR} \
		??/py-dissect.thumbcache@${PY_FLAVOR} \
		??/py-dissect.util@${PY_FLAVOR} \
		??/py-dissect.vmfs@${PY_FLAVOR} \
		??/py-dissect.volume@${PY_FLAVOR} \
		??/py-dissect.xfs@${PY_FLAVOR} \
		??/py-flow.record@${PY_FLAVOR} \
		??/py-fusepy@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/py-ruamel-yaml@${PY_FLAVOR} \
		??/py-structlog@${PY_FLAVOR} \
		??/py-zstandard@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
